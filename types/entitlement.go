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

// Entitlement entitlement
//
// swagger:model Entitlement
type Entitlement struct {

	// description
	Description string `json:"description,omitempty"`

	// feature access
	FeatureAccess interface{} `json:"feature_access,omitempty"`

	// href
	Href string `json:"href,omitempty"`

	// id
	// Required: true
	// Format: uuid
	ID *strfmt.UUID `json:"id"`

	// instance quota
	InstanceQuota interface{} `json:"instance_quota,omitempty"`

	// ip quota
	IPQuota interface{} `json:"ip_quota,omitempty"`

	// name
	Name string `json:"name,omitempty"`

	// project quota
	ProjectQuota int64 `json:"project_quota,omitempty"`

	// slug
	// Required: true
	Slug *string `json:"slug"`

	// volume limits
	VolumeLimits interface{} `json:"volume_limits,omitempty"`

	// volume quota
	VolumeQuota interface{} `json:"volume_quota,omitempty"`

	// weight
	// Required: true
	Weight *int64 `json:"weight"`
}

// Validate validates this entitlement
func (m *Entitlement) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateID(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateSlug(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateWeight(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *Entitlement) validateID(formats strfmt.Registry) error {

	if err := validate.Required("id", "body", m.ID); err != nil {
		return err
	}

	if err := validate.FormatOf("id", "body", "uuid", m.ID.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *Entitlement) validateSlug(formats strfmt.Registry) error {

	if err := validate.Required("slug", "body", m.Slug); err != nil {
		return err
	}

	return nil
}

func (m *Entitlement) validateWeight(formats strfmt.Registry) error {

	if err := validate.Required("weight", "body", m.Weight); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *Entitlement) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *Entitlement) UnmarshalBinary(b []byte) error {
	var res Entitlement
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}