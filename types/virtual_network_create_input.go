// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// VirtualNetworkCreateInput virtual network create input
//
// swagger:model VirtualNetworkCreateInput
type VirtualNetworkCreateInput struct {

	// description
	Description string `json:"description,omitempty"`

	// facility
	Facility string `json:"facility,omitempty"`

	// project id
	// Format: uuid
	ProjectID strfmt.UUID `json:"project_id,omitempty"`

	// vlan
	VLAN int64 `json:"vlan,omitempty"`

	// vxlan
	Vxlan int64 `json:"vxlan,omitempty"`
}

// Validate validates this virtual network create input
func (m *VirtualNetworkCreateInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateProjectID(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *VirtualNetworkCreateInput) validateProjectID(formats strfmt.Registry) error {

	if swag.IsZero(m.ProjectID) { // not required
		return nil
	}

	if err := validate.FormatOf("project_id", "body", "uuid", m.ProjectID.String(), formats); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *VirtualNetworkCreateInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *VirtualNetworkCreateInput) UnmarshalBinary(b []byte) error {
	var res VirtualNetworkCreateInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
